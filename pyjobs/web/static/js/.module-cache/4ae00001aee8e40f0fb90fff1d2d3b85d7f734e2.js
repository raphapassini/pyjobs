var JobsList = React.createClass({displayName: "JobsList",
    render: function() {
        return (
            React.createElement(JobItem, {title: "Trabalho Python", desc: "Descricao aqui"})
        );
    }
});

var JobItem = React.createClass({displayName: "JobItem",
    render: function() {
        React.createElement("div", {className: "panel panel-default"}, 
            React.createElement("div", {className: "panel-heading"}, this.params.job.title), 
            React.createElement("div", {className: "panel-body"}, 
                this.params.job.desc
            )
        )
    }
})