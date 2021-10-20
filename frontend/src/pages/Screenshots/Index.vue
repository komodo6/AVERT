<template>
  <div class="q-pa-sm screenshots">
    <q-toolbar>
      <q-input
        dark
        dense
        standout
        v-model="text"
        input-class="text-right"
        class=""
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

      <q-btn class="q-ma-md" color="grey-9" @click="switchViews">
        {{ viewState }}
      </q-btn>
    </q-toolbar>
    <div class="q-pa-md screenshots">
      <div class="row">
        <GalleryView
          v-show="gallView"
          v-for="(image, index) in images"
          :key="image.id"
          :index="index"
          v-bind="image"
        />
        <ListView v-show="listView" />
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from "vue";

import { useStore } from "vuex";
import GalleryView from "./GalleryView.vue";
import ListView from "./ListView.vue";
import axios from "axios";
export default {
  components: {
    GalleryView,
    ListView,
  },
  setup() {
    let store = useStore();

    let gallView = ref(true);
    let listView = ref(false);
    let viewState = ref("List View");
    let images = ref([]);
    const getImages = async () => {
      let { data } = await axios.get(
        "http://localhost:5000/screenshots/images"
      );
      console.log(data);
      store.state.screenshots.screenshots = data;
      images.value = store.state.screenshots.screenshots;
      console.log(images.value)
    };

    const switchViews = () => {
      if (gallView.value) {
        viewState.value = "Gallery View";
        gallView.value = false;
        listView.value = true;
      } else {
        viewState.value = "List View";
        gallView.value = true;
        listView.value = false;
      }
    };

    onMounted(() => {
      getImages();
    });

    return {
      images,
      text: ref(""),
      gallView,
      listView,
      viewState,
      switchViews,
    };
  },
};
</script>

<style lang="scss">
.screenshots {
  width: 100%;
  height: 100%;
}
</style>
