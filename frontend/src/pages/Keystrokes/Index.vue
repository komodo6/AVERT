<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table
          title="Keystrokes"
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
    name: "key",
    label: "Key",
    field: "key",
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
];

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

import axios from "axios";
import { onMounted, ref } from "vue";
import { exportFile, useQuasar } from "quasar";
export default {
  setup() {
    const $q = useQuasar();
    let rows = ref([]);
    const filter = ref("");
    onMounted(() => {
      fetchKeystrokes();
    });
    const fetchKeystrokes = async () => {
      const { data } = await axios.get("http://localhost:5000/keystrokes");
      rows.value = data;
      console.log(rows.value);
    };
    return {
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
