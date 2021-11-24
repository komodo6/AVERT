<template>
  <div class="q-px-lg">
    <div class="text-h4">Sync</div>
    <div class="row">
      <div class="col-5">
        <q-input outlined label="IP Address" v-model="ip" />
        <q-btn color="grey-9" class="q-mt-sm" label="Sync" @click="sync()" />
      </div>
    </div>
    <div class="row q-pt-sm">
      <div class="col-4 border" v-for="item in items" :key="item.label">
        <div class="text-body2">{{ item.label }}</div>
        <q-toggle color="primary" v-model="item.active" />
      </div>
      <div class="col-4 border">
        <div class="text-body2">Toggle All</div>
        <q-toggle color="primary" v-model="all" v-on:click="toggleAll()" />
      </div>
    </div>
  </div>
</template>
<script>
import { ref } from "vue";
import axios from "axios";
export default {
  setup() {
    let ip = ref("");
    let items = ref([
      { active: false, label: "Keystrokes" },
      { active: false, label: "Mouse" },
      { active: false, label: "Screenshots" },
      { active: false, label: "Processes" },
      { active: false, label: "Window History" },
      { active: false, label: "System Calls" },
      { active: false, label: "Video" },
      { active: false, label: "PCAP" },
    ]);
    let all = ref(false);
    const toggleAll = () => {
      if (all.value) {
        items.value.forEach((element) => {
          element.active = true;
        });
      } else {
        items.value.forEach((element) => {
          element.active = false;
        });
      }
    };

    const sync = async () => {
      let collections = [];
      for (const i of items.value) {
        if (i.active && i.label != "PCAP") {
          collections = collections.concat(i.label.replace(/\s/g, ""));
        } else if (i.active) {
          collections = collections.concat(["NetworkData", "NetworkPackets"]);
        }
      }
      let post_data = {
        collections: collections,
        ip: ip.value,
      };
      console.log(post_data);
      const response = await axios.post(
        "http://localhost:5000/sync/",
        post_data
      );
      console.log(response);
    };
    return {
      items,
      toggleAll,
      all,
      sync,
      ip,
    };
  },
};
</script>
<style lang="scss">
.border {
  border: 1px solid grey;
}
</style>
