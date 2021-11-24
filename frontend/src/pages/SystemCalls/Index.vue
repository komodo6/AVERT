<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table
          title="System Calls"
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
            <ExportData :rowData="rows" :headers="columns"/>
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
              <q-td key="SystemCallName" :props="props">
                {{ props.row.SystemCallName }}
              </q-td>
              <q-td key="SystemCallArgument" :props="props">
                {{ props.row.SystemCallArgument }}
              </q-td>
              <q-td key="SystemCallReturnValue" :props="props">
                {{ props.row.SystemCallReturnValue }}
              </q-td>
              <q-td key="SystemCallType" :props="props">
                {{ props.row.SystemCallType }}
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
    name: "SystemCallName",
    label: "SystemCall Name",
    field: "SystemCallName",
    align: "center",
    sortable: false,
  },
  {
    name: "SystemCallArgument",
    label: "SystemCall Argument",
    field: "SystemCallArgument",
    align: "center",
    sortable: true,
  },
  {
    name: "SystemCallReturnValue",
    label: "SystemCallReturn Value",
    field: "SystemCallReturnValue",
    align: "center",
    sortable: false,
  },
  {
    name: "SystemCallType",
    label: "SystemCall Type ",
    field: "SystemCallType",
    align: "center",
    sortable: false,
  },

];
import { api } from "src/boot/axios";
import { onMounted, ref } from "vue";
import { exportFile, useQuasar } from "quasar";
import ExportData from "../../components/ExportData.vue";


export default {
  components: {
    ExportData,
  },
  setup() {
    const updateTags = async (val, id) => {
      if (!val) {
        val = [];
      }
      await api.post("/systemcalls/systemcall", {
        id: id,
        tags: val,
      });
      console.log(val, id);
    };

    const $q = useQuasar();
    let rows = ref([]);
    const filter = ref("");

    onMounted(() => {
      fetchProcesses();
    });
    const fetchProcesses = async () => {
      const { data } = await api.get("/systemcalls");
      rows.value = data;
    };
    return {
      updateTags,
      filter,
      columns,
      rows,
    };
  },
};
</script>
