<template>
  <!-- <v-card-title>일기 로그</v-card-title> -->
  <div id="cal-heatmap"></div>
</template>
<script>
import CalHeatMap from "cal-heatmap";
import "cal-heatmap/cal-heatmap.css";
export default {
  mounted() {
    var cal = new CalHeatMap();
    cal.init({});
  },
};
</script>
