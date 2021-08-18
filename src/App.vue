<template>
  <div id="app">
    <Header />
    <div id="content" class="content">
      
    </div>
  </div>
</template>

<script>
import Header from './components/layout/Header.vue';
export default {
  name: "App",

  components:{
    Header,
  },

  data: () => ({}),
};
</script>
