import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    login: false,
    username: "",
    nickname: "",
    birthday: "",
    phone_number: "",
    address: "",
    token: null,
  },
  mutations: {
    GET_TOKEN(state, token) {
      state.login = true;
      state.username = token.username;
      state.nickname = token.nickname;
      state.birthday = token.birthday;
      state.phone_number = token.phone_number;
      state.address = token.address;
    },
  },
  actions: {},
  modules: {},
});
