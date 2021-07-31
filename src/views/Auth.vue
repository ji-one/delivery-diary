<template>
  <v-card class="mx-auto" max-width="400px">
    <v-card-title> SIGN IN </v-card-title>
    <v-card-actions>
      <kakao-login />
    </v-card-actions>
  </v-card>
</template>

<script>
import kakaoLogin from "../components/Auth/kakaoLogin";

export default { 
  name: "Auth",
  components: {
    kakaoLogin,
  },
};
</script>
<style></style>
