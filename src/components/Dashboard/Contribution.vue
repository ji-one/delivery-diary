<template>
  <v-card min-width="1000">
    <v-card-title class="justify-center"><div>일기 로그 📒</div></v-card-title>
    <v-card-subtitle class="text-center">
      <div>
        일기를 작성했던 날을 한 눈에 확인할 수 있어요. 색의 진하기는 그 날의
        일기 분량을 의미해요.
      </div>
      <div>
        해당 날짜를 클릭하면 그 날의 키워드들이 워드 클라우드로 나타나요!
      </div>
    </v-card-subtitle>
    <v-card-actions class="justify-center">
      <div id="cal-heatmap"></div>
    </v-card-actions>
  </v-card>
</template>
<script>
import CalHeatMap from "cal-heatmap";
import "cal-heatmap/cal-heatmap.css";
export default {
  data: () => ({
    isShow: false,
    calData: {},
  }),
  mounted() {
    this.axios.get("api/contribution").then((res) => {
      this.calData = res.data;
      this.initHeatMap();
    });
  },
  methods: {
    initHeatMap() {
      var cal = new CalHeatMap();
      cal.init({
        data: this.calData,
        domain: "year",
        subDomain: "day",
        cellSize: 15,
        tooltip: true,
        range: 1,
        start: new Date(new Date().setMonth(new Date().getMonth() - 6)),
        legend: [200, 400, 600, 800],
        // onClick: function() {
        //   console.log()
        // },
      });
    },
  },
};
</script>
