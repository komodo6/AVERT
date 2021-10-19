<template>
  <div>
    <q-table
      :columns="columns"
      selection="multiple"
      v-model="selectedScreenshots"
    >
    </q-table>
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
    name: "tags",
    label: "Tags",
    field: "tags",
    align: "center",
    sortable: true,
  },
];

export default {
  setup() {
    let selectedScreenshots = ref(null);
    return {
      columns,
      selectedScreenshots,
    };
  },
};
</script>
