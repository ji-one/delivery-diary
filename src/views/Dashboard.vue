<template>
  <v-container fill-height justify-center>
    <v-layout column align-center>
      <v-flex mt-10>
        <contribution />
      </v-flex>
      <v-flex mt-10>
        <chart />
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import Contribution from "@/components/Dashboard/Contribution.vue";
import Chart from "@/components/Dashboard/Chart.vue";
export default {
  components: {
    Contribution,
    Chart,
  },
};
</script>
