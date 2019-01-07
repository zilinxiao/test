<template>
  <div>
    <table class="table table-striped table-hover table-bordered">
      <thead>
        <tr>
          <th>序号</th>
          <th>用户姓名</th>
          <th>用户年龄</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user, index) in userlist" :key="index">
          <th v-text="index"/>
          <td v-text="user.name"></td>
          <td v-text="user.age"></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
export default {
    computed: {
      userlist() {
        return this.$store.state.userlist;
      }
  }
};
</script>
<style>
tr > th,
td {
  text-align: center;
}
</style>
