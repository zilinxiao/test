var app = new Vue({
    el: '#app1',
    data: {
        msg: "hello vue!",
        username: 'xzl',
        userage: 40,
        users:[]
    },
    created: function () {
        self = this;
        axios.get('/users').then(function (res) {
            self.users = res.data;
        });
    },
    methods: {
        adduser: function () {
            self = this;//防止username指向html元素
            axios.post('/add', {
                name: self.username,
                age: self.userage
            }).then(function (res) {
                self.users = res.data;
            })
        },
        updateuser: function () {
            self = this;//防止username指向html元素
            axios.put('/update', {
                name: self.username,
                age: self.userage
            }).then(function (res) {
                self.users = res.data;
            })
        },
        deleteuser: function () {
            self = this;//防止username指向html元素
            axios.delete('/delete/' + self.username
            ).then(function (res) {
                self.users = res.data;
            })
        },
        getusers: function () {
            self = this;
            axios.get('/users/'+self.username).then(function (res) {
                self.users = res.data;
            })
        }
    }
})