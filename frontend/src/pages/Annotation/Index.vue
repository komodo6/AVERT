<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table
          title="Annotations"
          :columns="columns"
          :rows="rows"
          :filter="filter"
          selection="multiple"
          v-model:selected="selected"
          row-key="id"
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
              <q-td>
                <q-checkbox v-model="props.selected"> </q-checkbox>
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
              <q-td key="annotations" :props="props">
                {{ props.row.annotations }}
              </q-td>
            </q-tr>
          </template>
        </q-table>
        <q-input class = "annotation" color = "amber" outlined v-model="text" label="Your Annotation" :dense="dense" />
        <q-btn class = "annotateBtn" color="grey-9 q-mx-sm" label = "Add Annotation"/>
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
    name: "annotations",
    label: "Annotations",
    name: "annotations",
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
    let selected = ref([]);
    const updateTags = async (val, id) => {
      if (!val) {
        val = [];
      }
      await axios.post("http://localhost:5000/keystrokes/keystroke", {
        id: id,
        tags: val,
      });
      console.log(val, id);
    };

    const $q = useQuasar();
    let rows = ref([]);
    const filter = ref("");

    onMounted(() => {
      fetchKeystrokes();
      fetchMouseactions();
      fetchSystemCalls();
      fetchProcesses();
    });
    const fetchKeystrokes = async () => {
      const { data } = await axios.get("http://localhost:5000/keystrokes");
      rows.value = data;
    };
    const fetchSystemCalls = async () => {
      const { data } = await axios.get("http://localhost:5000/systemcalls");
      rows.value.concat(data);
    };
    const fetchProcesses = async () => {
      const { data } = await axios.get("http://localhost:5000/processes");
      rows.value.concat(data);
    };
    const fetchMouseactions = async () => {
      const { data } = await axios.get("http://localhost:5000/mouseactions");
      rows.value.concat(data);
    };
    return {
      selected,
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

<style>
  .annotation{
    margin-top: 10px;
  }
  .annotateBtn{
    margin-top: 10px;
    float:right;
  }
</style>
