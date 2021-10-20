<template>
  <div class="col-auto q-pa-md">
    <q-card class="screenshot-card bg-grey-9">
      <q-img :src="'data:image/jpeg;base64,' + ScreenshotFile"> </q-img>

      {{ id }}
    </q-card>
  </div>
</template>

<script>
import { ref } from "vue";
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
    return {};
  },
};
</script>

<style lang="sass" scoped>
.screenshot-card
  width: 100%
  max-width: 250px
</style>
