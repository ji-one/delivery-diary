import { Doughnut } from "vue-chartjs";
export default {
  extends: Doughnut,
  mounted() {
    this.axios
      .get("api/analysis")
      .then((res) => {
        this.data = res.data;
        this.chartData.datasets[0].data = [
          this.data.very_positive,
          this.data.positive,
          this.data.neutral,
          this.data.negative,
          this.data.very_negative,
        ];
        this.renderChart(this.chartData, this.options);
        //console.log(this.data)
      })
      .catch((e) => console.log(e));
  },
  data: () => ({
    data: {},
    chartData: {
      hoverBackgroundColor: "red",
      labels: ["매우 긍정", "긍정", "중립", "부정", "매우 부정"],
      datasets: [
        {
          label: "Data One",
          backgroundColor: [
            "#5882FA",
            "#81BEF7",
            "#D8D8D8",
            "#F5A9BC",
            "#FA5858",
          ],
          data: [],
        },
      ],
    },
    options: {
      borderWidth: "20px",
      hoverBackgroundColor: "red",
      hoverBorderWidth: "10px",
    },
  }),
};
