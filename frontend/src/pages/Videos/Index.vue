<template>
  <div class="q-pa-sm Videos">
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
    <div class="q-pa-md Videos">
      <div class="row">
        <GalleryView
          v-show="gallView"
          v-for="video in videos"
          :key="video.id"
          v-bind="video"
        />
        <ListView v-show="listView" />
        <!-- <video class="video" controls>
          <source src="http://192.168.169.128:5000/videos/video?id=e79533a2-3c32-11ec-875d-000c29bb9f61.mp4" type="video/mp4">
        </video> -->
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from "vue";
import { useStore } from "vuex";
import GalleryView from "./GalleryView.vue";
import ListView from "./ListView.vue";
import { api } from "src/boot/axios";
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
    let videos = ref([]);
    const getImages = async () => {
      let { data } = await api.get(
        "/videos"
      );
      console.log(data);
      store.state.Videos.Videos = data;
      videos.value = store.state.Videos.Videos;
      console.log(videos.value);
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
      videos,
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
.Videos {
  width: 100%;
  height: 100%;
}
</style>
