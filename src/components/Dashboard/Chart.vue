<template>
  <v-card min-width="1000"
    ><v-card-title class="justify-center"><div>일기 분석 📊</div></v-card-title>
    <v-card-subtitle class="text-center">
      <div>
        한 달동안 작성한 일기 내용에 담긴 감정(긍정/부정/중립) 분석 결과를
        확인할 수 있어요.
      </div>
      <div>
        차트에 나타나는 숫자는 해당 감정을 나타내는 단어의 개수를 의미해요.
      </div>
    </v-card-subtitle>
    <v-card-actions class="justify-sm-space-around">
      <pie-chart></pie-chart>
      <v-div
        class="text-center"
        style="background-color: #f7f7f7; border-radius:10px; padding: 50px 20px"
      >
        <p>전체 분석된 단어 중 {{ this.ratio }}%가 긍정적인 의미에요.</p>
        <p>
          <body-1 v-html="this.message"> </body-1>
        </p>
      </v-div> </v-card-actions
  ></v-card>
</template>
<script>
import PieChart from "./PieChart.js";
export default {
  components: {
    PieChart,
  },
  mounted() {
    this.axios
      .get("api/analysis")
      .then((res) => {
        this.result = res.data;

        const total =
          this.result.very_positive +
          this.result.positive +
          this.result.negative +
          this.result.very_negative;

        this.ratio =
          ((this.result.very_positive + this.result.positive) / total).toFixed(
            1
          ) * 100;

        if (this.ratio >= 50) {
          this.message = "긍정적인 단어가 자주 보이네요! ❤️\n";
        } else
          this.message = "부정적인 단어가 긍적적인 단어보다 많아보여요.\n어떤 단어를 사용하느냐에 따라 느끼는 감정도 그 단어에 영향을 받는다고해요.\n 덜 부정적인, 나아가 긍정적인 느낌을 주는 말로 바꿔서 사용한다면,\n그에 맞게 감정도 변화시킬 수 있어요! 😇❤️"
            .split("\n")
            .join("<br />");
      })
      .catch((e) => console.log(e));
  },
  data: () => ({
    result: "",
    ratio: 0,
    message: "",
  }),
};
</script>
