<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col-12">
        <q-table
          :columns="columns"
          :rows="rows"
          selection="multiple"
          v-model:selected="selected"
          :filter="filter"
        >
          <template v-slot:top="">
            <!-- <div>
              <q-btn color="primary" class="q-ma-sm" @click="annotation = true"
                >Add Annotation</q-btn
              >
              <q-btn color="primary" class="q-ma-sm" @click="tag = true"
                >Add Tag</q-btn
              >
            </div> -->

            <q-input
              borderless
              dense
              debounce="300"
              v-model="filter"
              placeholder="Search"
            >
              <template v-slot:append>
                <q-icon name="search"> </q-icon>
              </template>
            </q-input>
            <q-btn
              class="q-mx-sm"
              color="primary"
              icon-right="archive"
              label="Export to csv"
              no-caps
              @click="exportTable"
            >
            </q-btn>
          </template>

          <template v-slot:body="props">
            <q-tr :props="props">
              <q-td>
                <q-checkbox v-model="props.selected" />
              </q-td>
              <q-td key="timestamp" :props="props">
                {{ props.row.timestamp }}
              </q-td>
              <q-td key="ip_address" :props="props">
                {{ props.row.ip_address }}
              </q-td>
              <q-td key="mac_address" :props="props">
                {{ props.row.mac_address }}
              </q-td>
              <q-td key="mac_address" :props="props">
                {{ props.row.pcapfile }}
              </q-td>
              <q-td key="mac_address" :props="props">
                {{ props.row.startTime }}
              </q-td>
              <q-td key="mac_address" :props="props">
                {{ props.row.endTime }}
              </q-td>
              <q-td key="annotations" :props="props">
                {{ props.row.annotations }}
                <q-popup-edit v-model="props.row.fat">
                  <q-input
                    type="textarea"
                    v-model="props.row.annotations"
                    dense
                    autofocus
                  />
                </q-popup-edit>
              </q-td>
              <q-td key="tags" :props="props">
                <q-select
                  label="Tags"
                  filled
                  :v="props.row.tags"
                  v-model="props.row.tags"
                  @update:model-value="updateTags(props.row.tags, props.row.id)"
                  use-input
                  use-chips
                  multiple
                  hide-dropdown-icon
                  input-debounce="0"
                  new-value-mode="add"
                  style="width: 250px"
                />
              </q-td>
            </q-tr>
          </template>
          <template v-slot:body-cell-action="props">
            <q-tr :props="props">
              <q-td>
                <q-btn
                  color="negative"
                  label="dasd"
                  no-caps
                  flat
                  dense
                  @click="packetView(props.row)"
                  >adadas</q-btn
                >
              </q-td>
            </q-tr>
          </template>
        </q-table>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        {{ packets }}
        <!-- <tree /> -->
      </div>
    </div>
    <!-- <div class="row">
      <div class="col-12">asda</div>
    </div> -->
    <q-dialog v-model="annotation">
      <q-card style="width: 700px; max-width: 80vw">
        <q-card-section>
          <div class="text-h6">Medium</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          Click/Tap on the backdrop.
        </q-card-section>

        <q-card-actions align="right" class="bg-white text-teal">
          <q-btn flat label="OK" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="tag">
      <q-card style="width: 700px; max-width: 80vw">
        <q-card-section>
          <div class="text-h6">Medium</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          Click/Tap on the backdrop.
        </q-card-section>

        <q-card-actions align="right" class="bg-white text-teal">
          <q-btn flat label="OK" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
import axios from "axios";
import tree from "./tree";
const columns = [
  {
    name: "timestamp",
    label: "Date/Tme",
    field: "timestamp",
    sortable: true,
    align: "center",
  },
  {
    name: "ip_address",
    label: "IP Address",
    field: "ip_address",
    align: "center",
    sortable: true,
  },
  {
    name: "mac_address",
    label: "MAC Address",
    field: "mac_address",
    align: "center",
    sortable: true,
  },
  {
    name: "pcapfile",
    label: "PCAP File",
    field: "pcapfile",
    align: "center",
    sortable: true,
  },
  {
    name: "startTime",
    label: "Start Time",
    field: "startTime",
    align: "center",
    sortable: true,
  },
  {
    name: "endTime",
    label: "End Time",
    field: "endTime",
    align: "center",
    sortable: true,
  },

  {
    name: "annotations",
    label: "Annotations",
    field: "annotations",
    align: "center",
    sortable: true,
  },
  {
    name: "tags",
    label: "Tags",
    field: "tags",
    align: "center",
    sortable: true,
  },
  { name: "action", label: "Action", field: "action" },
];
export default {
  components: {},
  setup() {
    const filter = ref("");
    let selected = ref([]);
    let rows = ref([]);
    let annotation = ref(false);
    let tag = ref(false);
    let packets = ref(null);
    const fetchPCAPS = async () => {
      let { data } = await axios.get("http://127.0.0.1:5000/networkdata");
      rows.value = data;
      console.log(data);
    };
    const fetchPackets = async () => {
      let { data } = await axios.get(
        "http://127.0.0.1:5000/networkdata/pcap?filename=ca89bba5-268f-459e-b44a-d18fb28af141.pcap"
      );
      packets.value = data;
    };

    const updateTags = async (val, id) => {
      if (!val) {
        val = [];
      }
      await axios.post("http://localhost:5000/screenshots/image", {
        id: id,
        tags: val,
      });
      console.log(val, id);
    };

    const packetView = (row) => {
      console.log(row);
    };

    onMounted(() => {
      // fetchData();
      fetchPCAPS();
      fetchPackets();
    });

    return {
      columns,
      rows,
      updateTags,
      selected,
      annotation,
      tag,
      packetView,
      packets,
      filter,
      exportTable() {
        // naive encoding to csv format
        const content = [columns.map((col) => wrapCsvValue(col.label))]
          .concat(
            rows.value.map((row) =>
              columns
                .map((col) =>
                  wrapCsvValue(
                    typeof col.field === "function"
                      ? col.field(row)
                      : row[col.field === void 0 ? col.name : col.field],
                    col.format
                  )
                )
                .join(",")
            )
          )
          .join("\r\n");

        const status = exportFile("keystrokes.csv", content, "text/csv");

        if (status !== true) {
          $q.notify({
            message: "Browser denied file download...",
            color: "negative",
            icon: "warning",
          });
        }
      },
    };
  },
};
</script>
