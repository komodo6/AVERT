<template>
  <div class="q-pt-md tree-view">
    <div>
      <q-input
        filled
        v-model="treeFilter"
        @update:model-value="updateTree"
        label="Filter"
      />
    </div>
    <div ref="treeView">></div>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
const JSONTreeView = require("json-tree-view");

export default {
  props: {
    packet: Object,
  },
  setup(props, context) {
    // let packet = ref(null);
    let treeView = ref(null);
    let treeFilter = ref(null);
    let tree = null;

    const updateTree = (value) => {
      tree.filterText = value;
    };

    onMounted(() => {
      tree = new JSONTreeView("", props.packet, null);
      tree.readonly = true;
      tree.expand(true);
      treeView.value.appendChild(tree.dom);
    });

    return {
      treeView,
      treeFilter,
      updateTree,
    };
  },
};
</script>

<style lang="scss">
.tree-view {
  background-color: $dark;
  height: 100%;
}
</style>
