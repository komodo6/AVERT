<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table
          title="WindowHistory"
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
              <q-td key="screen_res" :props="props">
                {{ props.row.screen_res }}
              </q-td>
              <q-td key="windo_pos" :props="props">
                {{ props.row.windo_pos }}
              </q-td>
              <q-td key="is_visible" :props="props">
                {{ props.row.is_visible }}
              </q-td>
              <q-td key="wp_command" :props="props">
                {{ props.row.wp_command }}
              </q-td>
              <q-td key="minimize" :props="props">
                {{ props.row.minimize }}
              </q-td>
              <q-td key="maximize" :props="props">
                {{ props.row.maximize }}
              </q-td>
              <q-td key="app_name" :props="props">
                {{ props.row.app_name }}
              </q-td>
              <q-td key="window_type" :props="props">
                {{ props.row.window_type }}
              </q-td>
              <q-td key="window_title" :props="props">
                {{ props.row.window_title }}
              </q-td>
              <q-td key="window_creation" :props="props">
                {{ props.row.window_creation }}
              </q-td>
              <q-td key="window_destruction" :props="props">
                {{ props.row.window_destruction }}
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
    name: "annotations",
    label: "Annotations",
    field: "annotations",
    align: "center",
    sortable: false,
  },
  {
    name: "tags",
    label: "Tags",
    field: "tags",
    align: "center",
    sortable: false,
  },
  {
    name: "screen_res",
    label: "Screen Resolution",
    field: "screen_res",
    align: "center",
    sortable: false,
  },
  {
    name: "window_pos",
    label: "Window Position",
    field: "window_pos",
    align: "center",
    sortable: false,
  },
  {
    name: "window_pos",
    label: "Window Position",
    field: "window_pos",
    align: "center",
    sortable: false,
  },
  {
    name: "is_visible",
    label: "Visible",
    field: "is_visible",
    align: "center",
    sortable: false,
  },
  {
    name: "wp_command",
    label: "Window Placement Command",
    field: "wp_command",
    align: "center",
    sortable: false,
  },
  {
    name: "minimize",
    label: "Minimized",
    field: "minimize",
    align: "center",
    sortable: false,
  },
  {
    name: "maximize",
    label: "Maximized",
    field: "maximize",
    align: "center",
    sortable: false,
  },
  {
    name: "app_name",
    label: "App Name",
    field: "app_name",
    align: "center",
    sortable: false,
  },
  {
    name: "window_type",
    label: "Window Type",
    field: "window_type",
    align: "center",
    sortable: false,
  },
  {
    name: "window_title",
    label: "Window Title",
    field: "window_title",
    align: "center",
    sortable: false,
  },
  {
    name: "window_creation",
    label: "Window Creation",
    field: "window_creation",
    align: "center",
    sortable: false,
  },
  {
    name: "window_destruction",
    label: "Window Destruction",
    field: "window_destruction",
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
      await axios.post("http://localhost:5000/windows/window", {
        id: id,
        tags: val,
      });
      console.log(val, id);
    };

    const $q = useQuasar();
    let rows = ref([]);
    const filter = ref("");

    onMounted(() => {
      fetchWindows();
    });
    const fetchWindows = async () => {
      const { data } = await axios.get("http://localhost:5000/windows");
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
