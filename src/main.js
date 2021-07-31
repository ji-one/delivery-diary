import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "vuetify/dist/vuetify.min.css";
import axios from "axios";
// import AxiosPlugin from 'vue-axios-cors';

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  axios,
  render: (h) => h(App),
}).$mount("#app");

window.Kakao.init("4b5757a81f0a599f1050ac0376ed87b7");
