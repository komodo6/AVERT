<template>
  <div class="col-auto q-pa-md">
    <q-card class="screenshot-card bg-grey-9">
      <q-img :src="url + image_id"> </q-img>
      {{ image_id }}
    </q-card>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  props: {
    image_id: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    return {
      url: ref("http://localhost:5000/screenshots/image?id="),
    };
  },
};
</script>

<style lang="sass" scoped>
.screenshot-card
  width: 100%
  max-width: 150px
</style>
