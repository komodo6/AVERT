<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table
          title="All Artifacts"
          :rows="rows"
          :columns="columns"
          row-key="name"
          dark
          color="amber"
          :rows-per-page-options="[]"


          scroll
        >
          <template v-slot:top>
            <q-input dark dense standout v-model="text" input-class="text-left" class="q-ml-md" label="Search" >
              <template v-slot:append>
                <q-icon v-if="text === ''" name="search" />
                <q-icon v-else name="clear" class="cursor-pointer" @click="text = ''" />
              </template>
            </q-input>
            <div class="item-selections row q-mx-sm">
              <div v-if="$q.screen.gt.xs" class="col">
                <q-checkbox v-model="visibleColumns" val="All" label="All" />
                <q-checkbox v-model="visibleColumns" val="Keystrokes" label="Keystrokes"/>
                <q-checkbox v-model="visibleColumns" val="Mouse Actions" label="Mouse Actions" /> <!-- q toggles are the toggles at the top-->
                <q-checkbox v-model="visibleColumns" val="Window Actions" label="Window Actions"/>
                <q-checkbox v-model="visibleColumns" val="System Calls" label="System Calls"/>
                <q-checkbox v-model="visibleColumns" val="Processes" label="Processes"/>
                <q-checkbox v-model="visibleColumns" val="PCAPs" label="PCAPs"/>
                <q-checkbox v-model="visibleColumns" val="Videos" label="Videos" />
                <q-checkbox v-model="visibleColumns" val="Screenshots" label="Screenshots" />
              </div>
            </div>

            <div class="row">
              <div class="datetime-from col-13" style = "padding: 15px">
                From:&nbsp;
                <input type="datetime-local" step = "1" name="Start" id="Start" />
              </div>
              <div class="datetime-to col-13" style = "padding: 15px">
                To:&nbsp;
                <input type="datetime-local" step = "1" name="End" id="End" />
              </div>
            </div>
              <q-input outlined v-model="text" dense = "dense" label="IP Address" style = "width: 350px; padding: 15px"/>
              <q-input outlined v-model="text" dense = "dense" label="MAC Address" style = "width: 350px; padding: 15px"/>
          </template>
        </q-table>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from "vue";

const columns = [
  { name: "Checkboxes", label: "_", field: "Checkboxes", align: "left" },
  { name: "Date", required: true, label: "Date", align: "left", field: (row) => row.name, format: (val) => `${val}`, sortable: true},
  { name: "Time", align: "center", label: "Time", field: "Time", sortable: true},
  { name: "DataType", label: "Data Type", field: "DataType"},
  { name: "MACAddress", label: "MAC Address", field: "MACAddress" },
  { name: "IPAddress", label: "IP Address", field: "IPAddress" },
];

const rows = [
  {name: "4/20/2021", Time: "13:50:30", DataType: "Mouse Action", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "4/20/2021", Time: "13:50:29", DataType: "Mouse Action", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "4/19/2021", Time: "12:55:23", DataType: "Keystroke", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "4/19/2021", Time: "12:55:23", DataType: "Keystroke", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "4/19/2021", Time: "12:55:23", DataType: "Keystroke", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "4/19/2021", Time: "12:55:23", DataType: "Process", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "4/19/2021", Time: "12:55:23", DataType: "System Call", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "4/19/2021", Time: "12:55:22", DataType: "Window Action", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "4/19/2021", Time: "12:55:22", DataType: "Mouse Action", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "4/19/2021", Time: "12:55:22", DataType: "Mouse Action", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "3/19/2021", Time: "13:45:22", DataType: "Process", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "3/19/2021", Time: "13:45:33", DataType: "Process", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "3/19/2021", Time: "13:45:32", DataType: "Process", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "3/19/2021", Time: "12:45:32", DataType: "PCAP", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "3/19/2021", Time: "12:45:32", DataType: "PCAP", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
  {name: "3/19/2021", Time: "12:45:32", DataType: "Keystroke", MACAddress: "30-65-EC-6F-C4-58", IPAddress: "129.102.99.234",},
];

export default defineComponent({
  setup() {
    let visibleColumns = ref(["Time","DataType","MACAddress","IPAddress","Date",]);
    const plusOne = computed(() => visibleColumns);
    console.log(plusOne);
    return {visibleColumns,rows,columns,text: ref(""),};
  },
});
</script>
