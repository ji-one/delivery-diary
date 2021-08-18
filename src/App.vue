<template>
  <v-app>
    <v-app-bar app color="blue-grey lighten-2" clipped-left>
      <v-spacer></v-spacer>
      <router-link to="/"></router-link>
      <v-btn v-if="!this.$store.state.login" text color="white" to="/signin"
        >SIGN IN</v-btn
      >
      <v-btn v-if="!this.$store.state.login" text color="white" to="/signup"
        >SIGN UP</v-btn
      >
      <v-btn v-if="this.$store.state.login" text color="white" @click="signout"
        >SIGN OUT</v-btn
      >
    </v-app-bar>
    <v-navigation-drawer app clipped>
      <v-list rounded>
        <v-list-item to="/">
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Home</v-list-item-title>
        </v-list-item>
        <v-list-item v-if="this.$store.state.login" to="/mypage">
          <v-list-item-icon>
            <v-icon>mdi-account</v-icon>
          </v-list-item-icon>
          <v-list-item-title>My Page</v-list-item-title>
        </v-list-item>
        <v-list-item to="/dashboard">
          <v-list-item-icon>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Dashboard</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({}),
  methods: {
    signout() {
      this.$store.commit("del_token");
      if (this.$route.path !== "/") this.$router.push({ name: "Home" });
    },
  },
};
</script>
