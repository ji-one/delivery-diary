import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Mypage from "../views/Mypage.vue";
import Dashboard from "../views/Dashboard.vue";
import list from "../views/list.vue";
import View from "@/views/View.vue"

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {path:"/", component: Home},
    {path:"/mypage", component: Mypage},
    {path:"/dashboard", component: Dashboard},
    {path:"/list", component: list},
    {path:"/board/view", component:View}
  ]
});

export default router;
