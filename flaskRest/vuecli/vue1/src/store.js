import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userlist: [
      { name: 'xzl', age: 35 },
      { name: 'ddp', age: 38 }
    ] //用户列表
  },
  mutations: {
    adduser(state, user) {
      const path = 'http://localhost:5000/add';
      axios.post(path, {
        name: user.name,
        age: user.age
      }).then(function (res) {
        state.userlist = res.data;
      })
    },
    updateuser(state, user) {
      const path = 'http://localhost:5000/update';
      axios.put(path, {
        name: user.name,
        age: user.age
      }).then(function (res) {
        state.userlist = res.data;
      })
    },
    deleteuser(state, user) {
      const path = 'http://localhost:5000/delete/';
      axios.delete(path + user.name
      ).then(function (res) {
        state.userlist = res.data;
      })
    },
    getusers(state, user) {
      const path = 'http://localhost:5000/users/';
      axios.get(path + user.name).then(function (res) {
        state.userlist = res.data;
      })
    },
    getallusers(state){
      const path = 'http://localhost:5000/users';
      axios.get(path).then(function (res) {
        state.userlist = res.data;
      })
    }
  },
  actions: {
    adduser({commit},user) {
      commit('adduser',user);
    },
    updateuser({commit},user){
      commit('updateuser',user)
    },
    deleteuser({commit},user){
      commit("deleteuser",user)
    },
    getusers({commit},user){
      commit("getusers",user)
    },
    getallusers({commit}){
      commit("getallusers")
    }
  }
})
