<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table
          title="Processes"
          :columns="columns"
          :rows="rows"
          row-key="id"
          selection="multiple"
          v-model:selected="selected"
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
            <ExportData :rowData="rows" :headers="columns" />
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
                <div
                  v-for="annotation in props.row.annotations"
                  :key="annotation"
                >
                  {{ annotation }}
                </div>
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
              <q-td key="proc_user" :props="props">
                {{ props.row.proc_user }}
              </q-td>
              <q-td key="proc_name" :props="props">
                {{ props.row.proc_name }}
              </q-td>
              <q-td key="proc_pid" :props="props">
                {{ props.row.proc_pid }}
              </q-td>
              <q-td key="proc_parent" :props="props">
                {{ props.row.proc_parent }}
              </q-td>
              <q-td key="proc_time_created" :props="props">
                {{ props.row.proc_time_created }}
              </q-td>
              <q-td key="proc_cmdline" :props="props">
                {{ props.row.proc_cmdline }}
              </q-td>
              <q-td key="proc_terminal" :props="props">
                {{ props.row.proc_terminal }}
              </q-td>
              <q-td key="proc_status" :props="props">
                {{ props.row.proc_status }}
              </q-td>
              <q-td key="proc_memory_percentage" :props="props">
                {{ props.row.proc_memory_percentage }}
              </q-td>
              <q-td key="proc_threads" :props="props">
                {{ props.row.proc_threads }}
              </q-td>
              <q-td key="proc_cpu_percentage" :props="props">
                {{ props.row.proc_cpu_percentage }}
              </q-td>
              <q-td key="proc_privileges" :props="props">
                {{ props.row.proc_privileges }}
              </q-td>
              <q-td key="proc_priority" :props="props">
                {{ props.row.proc_priority }}
              </q-td>
              <q-td key="proc_type" :props="props">
                {{ props.row.proc_type }}
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
    name: "proc_user",
    label: "Process User",
    field: "proc_user",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_name",
    label: "Process Name",
    field: "proc_name",
    align: "center",
    sortable: true,
  },
  {
    name: "proc_pid",
    label: "Process PID",
    field: "proc_pid",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_parent",
    label: "Process PPID",
    field: "proc_parent",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_time_created",
    label: "Process Start Time",
    field: "proc_time_created",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_cmdline",
    label: "Process Comand",
    field: "proc_cmdline",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_terminal",
    label: "Process Terminal",
    field: "proc_terminal",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_status",
    label: "Process Status",
    field: "proc_status",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_memory_percentage",
    label: "Process Memory",
    field: "proc_memory_percentage",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_threads",
    label: "Process Threads",
    field: "proc_threads",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_cpu_percentage",
    label: "Process CPU Usage",
    field: "proc_cpu_percentage",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_privileges",
    label: "Process Privileges",
    field: "proc_privileges",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_priority",
    label: "Process Priority",
    field: "proc_priority",
    align: "center",
    sortable: false,
  },
  {
    name: "proc_type",
    label: "Process Type",
    field: "proc_type",
    align: "center",
    sortable: false,
  },
];
import axios from "axios";
import { onMounted, ref } from "vue";
import { exportFile, useQuasar } from "quasar";
import ExportData from "../../components/ExportData.vue";
import { fetchProcesses, updateTags } from "src/utils/request.js";
import avertStore from "src/avertStore";

export default {
  components: {
    ExportData,
  },
  setup() {
    const $q = useQuasar();
    let rows = ref([]);
    const filter = ref("");
    let selected = ref([]);

    fetchProcesses();
    rows.value = avertStore.state.processes;
    return {
      updateTags,
      filter,
      columns,
      rows,
      selected,
    };
  },
};
</script>
