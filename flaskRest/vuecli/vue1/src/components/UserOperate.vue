<template>
  <div>
    <div class="form-group row">
      <label for="username" class="col-sm-2">用户姓名</label>
      <div class="col-sm-10">
        <input type="text" name="username" id="username" class="form-control" v-model="username">
      </div>
    </div>
    <div class="form-group row">
      <label for="userage" class="col-sm-2">用户年龄</label>
      <div class="col-sm-10">
        <input type="number" name="userage" id="userage" class="form-control" v-model="userage">
      </div>
    </div>
    <div id="btns">
      <label class="col-sm-2"></label>
      <button type="button" class="btn btn-success" v-on:click="adduser">添加</button>
      <button type="button" class="btn btn-success" v-on:click="updateuser">更新</button>
      <button type="button" class="btn btn-success" v-on:click="deleteuser">删除</button>
      <button type="button" class="btn btn-success" v-on:click="getusers">查询</button>
      <button type="button" class="btn btn-success" v-on:click="getallusers">全部用户</button>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      username: "xzl",
      userage: 35
    };
  },
  methods: {
    adduser() {
      let user = {
        name: this.username,
        age: this.userage
      };
      this.$store.dispatch("adduser", user);
    },
    updateuser() {
      let user = {
        name: this.username,
        age: this.userage
      };
      this.$store.dispatch("updateuser", user);
    },
    getusers() {
      let user = {
        name: this.username,
        age: this.userage
      };
      this.$store.dispatch("getusers", user);
    },
    deleteuser() {
      let user = {
        name: this.username,
        age: this.userage
      };
      this.$store.dispatch("deleteuser", user);
    },
    getallusers(){
      this.$store.dispatch("getallusers");
      this.$router.push('users');
    }
  }
};
</script>
<style>
div#btns > button {
  margin-right: 2rem;
  width: 5rem;
}
</style>
