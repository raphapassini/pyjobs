function create_react_component(domElementId, component) {
    var node = document.getElementById(domElementId)

    if( !node )
        return false

    React.render(
        React.createElement(component, null),
        node
    );
}

create_react_component('react-jobs-table', JobsList)