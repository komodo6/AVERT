<template>
  <div class="q-pa-sm">
    <!-- <div class="row">
      <div class="col">
        <q-table
          title="All Acts"
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

            
          </template>


        </q-table>
      </div>
    </div> -->
    <div class="row">
      <div class="col">
        Start Time
        <div class="datetime-from col-12">
          <input v-model="dateTimeFrom" type="datetime-local" step="0.001" name="" id="" />
        </div>
      </div>

      <div class="col">
        End Time
        <div class="datetime-to col-12">
          <input v-model="dateTimeTo" type="datetime-local" step="0.001" name="" id="" />
        </div>
      </div>
    </div>
    <div class="row">
      <q-btn @click="sendDates" color="white" text-color="black" label="GENERATE" />
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
  data(){
    return{
      dateTimeFrom: ref(""),
      dateTimeTo: ref("")
    }
  },
  methods:{
    sendDates(){
      console.log("This dateTimeFrom " + this.dateTimeFrom)
      console.log("This dataTimeTo " + this.dateTimeTo)
      console.log('Sending Dates')
    }

  }
};
</script>
