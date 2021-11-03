<template>
  <div>
    <q-table
      :columns="columns"
      :rows="Videos"
      v-model="selectedVideos"
      row-key="name"
    >
      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td key="timestamp" :props="props">
            {{ props.row.timestamp }}
          </q-td>
          <q-td key="filename" :props="props">
            {{ props.row.filename }}
          </q-td>
          <q-td key="resolution" :props="props">
            {{ props.row.resultion }}
          </q-td>
          <q-td key="frame_rate" :props="props">
            {{ props.row.frame_rate }}
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
        </q-tr>
      </template>
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
    name: "filename",
    label: "File Name",
    field: "filename",
    align: "center",
    sortable: true,
  },
  {
    name: "resolution",
    label: "Resolution",
    field: "resolution",
    align: "center",
    sortable: true,
  },
  {
    name: "frame_rate",
    label: "Frame Rate",
    field: "frame_rate",
    align: "center",
    sortable: true,
  },
  {
    name: "annotations",
    label: "Annotations",
    field: "annotations",
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
import { ref, computed } from "vue";
import { useStore } from "vuex";
import axios from "axios";
export default {
  setup() {
    let store = useStore();

    let Videos = computed(() => store.state.screenshots.screenshots);

    let selectedVideos = ref(null);

    const updateTags = async (val, id) => {
      if (!val) {
        val = [];
      }
      await axios.post("http://127.0.0.1:5000/Videos/video", {
        id: id,
        tags: val,
      });
      console.log(val, id);
    };
    return {
      updateTags,
      Videos,
      columns,
      selectedVideos,
    };
  },
};
</script>
