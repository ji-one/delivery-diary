<template>
  <v-app :style="{ background: $vuetify.theme.themes.light.background }">
    <v-app-bar app color="blue lighten-4">
      <router-link to="/">
        <v-btn icon>
          <v-icon>mdi-home</v-icon>
        </v-btn></router-link
      >
      <v-spacer></v-spacer>
      <!-- TODO refactor: 버튼 속성 코드 중복 -->
      <v-btn
        v-if="!this.$store.state.login"
        class="font-weight-bold"
        color="blue-grey darken-1"
        large
        rounded
        text
        to="/signup"
        >계정 만들기</v-btn
      >
      <v-btn
        v-if="!this.$store.state.login"
        class="font-weight-bold"
        color="blue-grey darken-1"
        large
        rounded
        text
        to="/signin"
        >로그인</v-btn
      >
      <v-btn
        v-if="this.$store.state.login"
        class="font-weight-bold"
        color="blue-grey darken-1"
        large
        rounded
        text
        >배송 현황</v-btn
      >
      <v-btn
        v-if="this.$store.state.login"
        class="font-weight-bold"
        color="blue-grey darken-1"
        large
        rounded
        text
        to="/dashboard"
        >MY DASHBOARD</v-btn
      >
      <v-menu offset-y v-if="this.$store.state.login">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            class="font-weight-bold"
            color="blue-grey darken-1"
            large
            rounded
            text
            v-bind="attrs"
            v-on="on"
          >
            <profile />
          </v-btn>
        </template>
        <v-list>
          <v-list-item to="/mypage">
            <v-list-item-title>내 정보</v-list-item-title>
          </v-list-item>
          <v-list-item @click="signout">
            <v-list-item-title>로그아웃</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
    <v-footer></v-footer>
  </v-app>
</template>
<script>
import profile from "./components/App/Profile";
export default {
  name: "App",
  data: () => ({}),
  components: {
    profile,
  },
  methods: {
    signout() {
      this.$store.commit("del_token");
      if (this.$route.path !== "/") this.$router.push({ name: "Home" });
    },
  },
};
</script>
