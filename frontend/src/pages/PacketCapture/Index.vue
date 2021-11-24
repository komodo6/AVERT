<template>
  <div class="q-pa-sm" v-if="!packfileview">
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
              <q-td key="action" :props="props">
                <q-btn @click="openPacketFile(props.row)" color="grey-9"
                  >Open Packet File</q-btn
                >
              </q-td>
            </q-tr>
          </template>
        </q-table>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <!-- {{ packets }} -->
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
  <div v-else>
    <PacketCaptureFileView
      @back="packfileview = !packfileview"
      :pcapfile="pcapfile"
    />
  </div>
</template>

<script>
import { onMounted, ref, defineComponent } from "vue";
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

import { useRouter } from "vue-router";
import PacketCaptureFileView from "./PacketFileView.vue";
// import route from "src/router";
export default defineComponent({
  components: { PacketCaptureFileView },
  setup() {
    const filter = ref("");
    let selected = ref([]);
    let rows = ref([]);
    let annotation = ref(false);
    let tag = ref(false);
    let packets = ref(null);
    let packfileview = ref(false);
    let pcapfile = ref(null);
    const router = useRouter();
    const fetchPCAPS = async () => {
      let { data } = await axios.get("http://192.168.169.128:5000/networkdata");
      rows.value = data;
      console.log(data);
    };
    const fetchPackets = async () => {
      let { data } = await axios.get(
        "http://192.168.169.128:5000/networkdata/pcap?filename=9119e12c-5b1f-4924-a052-637806a6610d.pcap"
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

    const openPacketFile = (row) => {
      console.log(row);
      packfileview.value = true;
      pcapfile.value = row.pcapfile;
      // console.log(route);
      // router.push({
      //   name: "PacketCaptureFileView",
      //   params: {
      //     pcapfile: row.pcapfile,
      //   },
      // });
    };

    onMounted(() => {
      // fetchData();
      fetchPCAPS();
      fetchPackets();
    });

    return {
      pcapfile,
      packfileview,
      columns,
      rows,
      updateTags,
      selected,
      annotation,
      tag,
      openPacketFile,
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
});
</script>
