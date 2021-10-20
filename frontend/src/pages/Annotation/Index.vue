                                                                                                <template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table
          title="Annotations"
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
          </template>
          <template v-slot:body="props ">
          <q-tr :props="props" @click="props.selected = true">
        <q-td>
          <q-checkbox v-model="props.selected" color="primary" />
        </q-td>
        <q-td v-for="col in props.cols" :key="col.name" :props="props">{{
          col.value
        }}</q-td>
      </q-tr>
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
              <q-td key="Type" :props="props">
                {{ props.row.Type }}
              </q-td>
              <q-td key="key" :props="props">
                {{ props.row.key }}

              </q-td> <!-- Need to update the above to get the data type-->
            </q-tr>
          </template>
        </q-table>
        <q-input class = "annotation" color = "amber" outlined v-model="text" label="Your annotation" />
        <q-btn class = "annotateBtn" style="width: 200px" label="Add Annotation" color="grey-9 q-mx-sm" push/>
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
    name: "Selected",
    label: "Selected",
    field: "Selected",
    align: "center",
    sortable: true,
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
    name: "Type",
    label: "Type",
    field: "Type",
    align: "center",
    sortable: true,
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
