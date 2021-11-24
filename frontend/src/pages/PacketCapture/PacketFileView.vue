<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col-12">
        <q-table
          :columns="columns"
          :rows="rows"
          :filter="filter"
          selection="single"
          row-key="timestamp"
          v-model:selected="selected"
          @update:selected="showTree"
        >
          <template v-slot:top-left>
            <q-btn @click="backToFileView" color="red" icon="arrow_back_ios">
            </q-btn>
          </template>
          <template v-slot:top-right>
            <q-input
              borderless
              dense
              debounce="300"
              v-model="filter"
              placeholder="Search"
              filled
            >
              <template v-slot:append>
                <q-icon name="search"> </q-icon>
              </template>
            </q-input>
          </template>
          <template v-slot:body="props">
            <q-tr :props="props">
              <q-td>
                <q-checkbox v-model="props.selected" />
              </q-td>
              <q-td key="timestamp" :props="props">
                {{ props.row.timestamp }}
              </q-td>

              <q-td key="filestream" :props="props">
                {{ props.row.filestream }}
              </q-td>
              <q-td key="rawHexByte" :props="props">
                {{ props.row.rawHexByte }}
              </q-td>
            </q-tr>
          </template>
        </q-table>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <tree v-if="selected.length" :packet="packet" />
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted, ref, defineComponent } from "vue";
import { api } from "src/boot/axios";
import tree from "./tree";
const columns = [
  {
    name: "timestamp",
    label: "Date/Tme",
    field: "timestamp",
    sortable: true,
    align: "center",
  },

  {
    name: "filestream",
    label: "File Steam",
    field: "filestream",
    align: "center",
    sortable: true,
  },
  {
    name: "rawHexByte",
    label: "Raw Hex",
    field: "rawHexByte",
    align: "left",
    sortable: true,
  },
];
export default defineComponent({
  props: {
    pcapfile: {
      type: String,
      required: true,
    },
  },
  components: {
    tree,
  },
  setup(props, context) {
    let selected = ref([]);
    let rows = ref([]);
    let filter = ref(null);

    let packet = ref(null);

    const fetchPackets = async (filename) => {
      let { data } = await api.get(
        "/networkdata/pcap",
        {
          params: {
            filename: filename,
          },
        }
      );
      rows.value = data;
      console.log(data);
    };

    const backToFileView = () => {
      context.emit("back");
    };

    const updateTags = async (val, id) => {
      if (!val) {
        val = [];
      }
      await api.post("/screenshots/image", {
        id: id,
        tags: val,
      });
      console.log(val, id);
    };

    const showTree = (selection) => {
      packet.value = selection[0];
    };

    onMounted(() => {
      console.log(props);
      fetchPackets(props.pcapfile);
      // fetchData();
      // fetchPCAPS();
    });

    return {
      showTree,
      packet,
      columns,
      rows,
      backToFileView,

      selected,

      filter,
    };
  },
});
</script>
