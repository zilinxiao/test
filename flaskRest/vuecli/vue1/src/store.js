import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userlist:[
      {name:'xzl',age:35},
      {name:'ddp',age:38}
    ] //用户列表
  },
  mutations: {
    adduser(state,user){
      state.userlist.push(user);
    }
  },
  actions: {
    adduser (context){
      context.commit('adduser');
    }
  }
})
