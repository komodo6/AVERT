<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table
          title="All Artifacts"
          :rows="rows"
          :columns="columns"
          dark
          color="amber"
          selection="multiple"
          v-model:selected="selected"
          row-key="id"
        >
          <template v-slot:top>
            <q-input
              dark
              dense
              standout
              v-model="text"
              input-class="text-right"
              class="q-ml-md"
              label="Search"
            >
              <template v-slot:append>
                <q-icon v-if="text === ''" name="search" />
                <q-icon
                  v-else
                  name="clear"
                  class="cursor-pointer"
                  @click="text = ''"
                />
              </template>
            </q-input>

            <div class="row">
              <div class="datetime-from col-12">
                <input type="datetime-local" name="" id="" />
              </div>
              <div class="datetime-to col-12">
                <input type="datetime-local" name="" id="" />
              </div>
            </div>
          </template>

          <template v-slot:body="props">
            <q-tr :props="props">
              <q-td>
                <q-checkbox v-model="props.selected" />
              </q-td>
              <q-td key="timestamp" :props="props"
                ><!--This is the line to add the checkboxes to the rows-->
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
              </q-td>
              <!-- Need to update the above to get the data type-->
            </q-tr>
          </template>
        </q-table>
      </div>
    </div>
  </div>
</template>

<script>
// const { desktopCapturer } = require("electron");
import { defineComponent, ref, computed, onMounted } from "vue";

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
    name: "Type",
    label: "Type",
    field: "Type",
    align: "center",
    sortable: true,
  },
];

import axios from "axios";

import { exportFile, useQuasar } from "quasar";

export default {
  setup() {
    let selected = ref([]);
    let visibleColumns = ref([
      "calories",
      "desc",
      "fat",
      "carbs",
      "protein",
      "sodium",
      "calcium",
      "iron",
    ]);

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

    let rows = ref([]);

    onMounted(() => {
      fetchKeystrokes();
      fetchMouseactions();
      fetchSystemCalls();
      fetchProcesses();
    });

    const plusOne = computed(() => visibleColumns);
    console.log(plusOne);
    return {
      selected,
      visibleColumns,
      rows,
      columns,
      text: ref(""),
    };
  },
};
</script>
