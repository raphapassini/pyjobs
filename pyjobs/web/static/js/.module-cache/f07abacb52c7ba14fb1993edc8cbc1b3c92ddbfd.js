var JobsList = React.createClass({displayName: "JobsList",
    render: function() {
        var job = {
            'title': 'Raphael',
            'desc': 'abc'
        }

        return (
            React.createElement(JobItem, {job: job})
        );
    }
});

var JobItem = React.createClass({displayName: "JobItem",
    render: function() {
        React.createElement("div", {className: "panel panel-default"}, 
            React.createElement("div", {className: "panel-heading"}, this.props.job.title), 
            React.createElement("div", {className: "panel-body"}, 
                this.props.job.desc
            )
        )
    }
})