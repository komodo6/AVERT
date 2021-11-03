<template>
  <div class="q-pa-sm videos">
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
    
    <div class="q-pa-md videos">
      <div class="row">
        <GalleryView
          v-show="gallView"
          v-for="image in images"
          :key="image.id"
          v-bind="image"
        />
        <ListView v-show="listView" />
      </div> 
      <q-video src="http://127.0.0.1:5000/videos/video?id=e79533a2-3c32-11ec-875d-000c29bb9f61.mp4" class="video" />
        <video class="video" controls>
        <source src="http://127.0.0.1:5000/videos/video?id=e79533a2-3c32-11ec-875d-000c29bb9f61.mp4" type="video/mp4"> 
        </video>
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
    // let { data } = await axios.get(
    //     "http://127.0.0.1:5000/videos/video?id=e79533a2-3c32-11ec-875d-000c29bb9f61.mp4"
    //   );
    //   console.log(data);
    //   store.state.screenshots.screenshots = data;
    //   images.value = store.state.screenshots.screenshots;
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

