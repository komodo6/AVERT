<template>
  <div class="col-auto q-pa-md">
    <q-card class="screenshot-card bg-grey-9">
      <q-img :src="'data:image/jpeg;base64,' + ScreenshotFile"> </q-img>
      <q-card-section>
        {{ id }}
      </q-card-section>
      <q-card-actions align="center">
        <a
          :href="'data:image/jpeg;base64,' + ScreenshotFile"
          :download="id + '.png'"
          ><q-btn> download </q-btn></a
        >

        <q-btn flat @click="deleteIMG(id)">Delete</q-btn>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
import { ref } from "vue";
import axios from "axios";
import { useStore } from "vuex";
export default {
  props: {
    id: {
      type: String,
      required: true,
    },
    ScreenshotFile: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    let store = useStore();
    const deleteIMG = async (id) => {
      let { data } = await axios.delete(
        "http://192.168.169.128:5000/screenshots/image/" + id
      );
      console.log(data);
      store.state.screenshots.screenshots.forEach((element, index) => {
        if (element.id == id) {
          store.state.screenshots.screenshots.splice(index, 1);
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
-
