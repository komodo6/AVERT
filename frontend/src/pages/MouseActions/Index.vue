<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table
          title="Mouse Actions"
          :columns="columns"
          :rows="rows"
          row-key="id"
          :filter="filter"
        >
          <template v-slot:top-right>
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
              <q-td key="timestamp" :props="props">
                {{ props.row.timestamp }}
              </q-td>
              <q-td key="ip_address" :props="props">
                {{ props.row.ip_address }}
              </q-td>
              <q-td key="mac_address" :props="props">
                {{ props.row.mac_address }}
              </q-td>
              <q-td key="type" :props="props">
                {{ props.row.type }}
              </q-td>
              <q-td key="coords" :props="props">
                {{ props.row.coords }}
              </q-td>
              <q-td key="pressed" :props="props">
                {{ props.row.pressed }}
              </q-td>
              <q-td key="scroll" :props="props">
                {{ props.row.scroll }}
              </q-td>
              <q-td key="active_window" :props="props">
                {{ props.row.active_window }}
              </q-td>
              <q-td key="annotations" :props="props">
                {{ props.row.annotations }}
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
        </q-table>
      </div>
    </div>
  </div>
</template>

<script>
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
    name: "type",
    label: "Type",
    field: "type",
    align: "center",
    sortable: true,
  },
  {
    name: "coords",
    label: "Coordinates",
    field: "coords",
    align: "center",
    sortable: true,
    format: (val, row) => val.join(", "),
  },
  {
    name: "pressed",
    label: "Pressed",
    field: "pressed",
    align: "center",
    sortable: true,
  },
  {
    name: "scroll",
    label: "Scroll",
    field: "scroll",
    align: "center",
    sortable: true,
  },
  {
    name: "active_window",
    label: "Window",
    name: "active_window",
    align: "center",
    sortable: false,
  },
  {
    name: "annotations",
    label: "Annotations",
    name: "annotations",
    align: "center",
    sortable: false,
  },
  {
    name: "tags",
    label: "Tags",
    name: "tags",
    align: "center",
    sortable: false,
  },
];
import axios from "axios";
import { onMounted, ref } from "vue";
import { exportFile, useQuasar } from "quasar";

function wrapCsvValue(val, formatFn) {
  let formatted = formatFn !== void 0 ? formatFn(val) : val;

  formatted =
    formatted === void 0 || formatted === null ? "" : String(formatted);

  formatted = formatted.split('"').join('""');
  /**
   * Excel accepts \n and \r in strings, but some other CSV parsers do not
   * Uncomment the next two lines to escape new lines
   */
  // .split('\n').join('\\n')
  // .split('\r').join('\\r')

  return `"${formatted}"`;
}

export default {
  setup() {
    const updateTags = async (val, id) => {
      if (!val) {
        val = [];
      }
      await axios.post("http://localhost:5000/mouseactions/mouseaction", {
        id: id,
        tags: val,
      });
      console.log(val, id);
    };

    const $q = useQuasar();
    let rows = ref([]);
    const filter = ref("");

    onMounted(() => {
      fetchMouseactions();
    });
    const fetchMouseactions = async () => {
      const { data } = await axios.get("http://localhost:5000/mouseactions");
      rows.value = data;
    };
    return {
      updateTags,
      filter,
      columns,
      rows,
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

        console.log(content)

        const status = exportFile("mouseactions.csv", content, "text/csv");

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
