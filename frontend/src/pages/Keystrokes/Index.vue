<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table title="Keystrokes" :columns="columns"> </q-table>
      </div>
    </div>
  </div>
</template>

<script>
const columns = [
  {
    name: "timestamp",
    label: "Date/Tme",
    sortable: true,
    align: "center",
  },
  {
    name: "IP Address",
    label: "IP Address",
    align: "center",
    sortable: true,
  },
  {
    name: "MAC Address",
    label: "MAC Address",
    align: "center",
    sortable: true,
  },
  {
    name: "Key",
    label: "Key",
    align: "center",
    sortable: true,
  },
  {
    name: "Window",
    label: "Window",
    align: "center",
    sortable: true,
  },
];
export default {
  setup() {
    return {
      columns,
    };
  },
};
</script>
