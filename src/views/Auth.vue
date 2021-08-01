<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="5">
        <component :is="component"></component>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Auth",
  data: () => ({ component: null }),
  created() {
    this.loadComponent();
  },
  watch: {
    $route(to, from) {
      if (to.path !== from.path) {
        this.loadComponent();
      }
    },
  },
  methods: {
    loadComponent() {
      switch (this.$route.path) {
        case "/signin":
          this.component = () => import("../components/Auth/SignIn.vue");
          break;
        case "/signup":
          this.component = () => import("../components/Auth/SignUp.vue");
          break;
        default:
          this.component = null;
      }
    },
  },
};
</script>
<style></style>
