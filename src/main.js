import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import store from "./store";
import http from "./js/http";

Vue.config.productionTip = false;
Vue.prototype.$http = http;

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount("#app");
