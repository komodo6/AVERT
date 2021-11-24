<template>
  <div class="col-auto q-pa-md">
    <q-card class="video-card bg-grey-9">
      <q-video :src="`http://localhost:5000/videos/video?id=${filename}`">
      </q-video>

      <q-card-section>
        {{ filename }}
      </q-card-section>
      <q-card-actions align="center">
        <q-btn flat @click="deleteIMG(id)">Delete</q-btn>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
import { api } from "src/boot/axios";
import { useStore } from "vuex";
export default {
  props: {
    id: {
      type: String,
      required: true,
    },
    filename: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    let store = useStore();
    const deleteIMG = async (id) => {
      let { data } = await api.delete(
        "/videos/video?id=" + id
      );
      console.log(data);
      store.state.Videos.Videos.forEach((element, index) => {
        if (element.id == id) {
          store.state.Videos.Videos.splice(index, 1);
        }
      });
    };
    return {
      deleteIMG,
    };
  },
};
</script>

<style lang="sass" scoped>
.screenshot-card
  width: 100%
  max-width: 250px
.q-btn:hover
  background-color: red
.q-btn
  flex: 1
</style>
