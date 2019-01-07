<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <UserOperate/>
    <hr>
    <UserTable />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import UserTable from "@/components/UserTable.vue";
import UserOperate from "@/components/UserOperate.vue";

export default {
  name: "home",
  components: {
    // HelloWorld
    UserTable,
    UserOperate
  },
  data() {
    return {
      userlist: [
        {
          name: "xzl",
          age: 35
        }
      ]
    };
  }
};
</script>
