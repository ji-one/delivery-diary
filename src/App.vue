<template>
  <v-app>
    <v-app-bar app color="blue-grey lighten-2" clipped-left>
      <v-spacer></v-spacer>
      <router-link to="/"></router-link>
      <v-btn text color="white" to="/signin">SIGN IN</v-btn>
      <v-btn text color="white" to="/signup">SIGN UP</v-btn>
    </v-app-bar>
    <v-navigation-drawer app clipped>
      <v-list rounded>
        <v-list-item to="/mypage">
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
};
</script>
