var React = require('react')
var ReactDOM = require('react-dom')


import Content from './content.jsx'
import SideBarEle from './sidebarele.jsx'

export default class LandingPage extends React.Component {
    constructor(props) {    /* Note props is passed into the constructor in order to be used */
      super(props);
      this.state = { curUser : props.profile_info.data,
                    curElement : 0,
                    sideBarContents : (props.profile_info.data.level === "TRAINER") ?
                    ["My Profile", "My Trainees", "Calendar","Saved Workouts", "Trainee Nearby", "Settings"] :
                    ["My Profile", "Calendar","Saved Workouts", "Settings"]};

    }
    onSideBarClick(index){
        this.setState({curElement : index});
    }
    componentDidMount(){
    }
    render(){
        console.log(this.state.curUser);
        var sideBarEle = this.state.sideBarContents.map(function(ele, i){
            var boundClick = this.onSideBarClick.bind(this,i);
            return(<SideBarEle text={ele} onClick={boundClick} curElement={this.state.curElement} key={i} eleIndex ={i}/>);
        },this);
        var contentDisplay = <Content curContent={this.state.sideBarContents[this.state.curElement]} curUser={this.state.curUser}/>
        return (
            <header>
            <div>
                <div className="side-bar-parent">
                    <ul id="nav-mobile" className="side-nav fixed">
                        {sideBarEle}
                    </ul>
                </div>
                <div className="content-panel-parent">
                <main>

                <nav>
                <div className="nav-wrapper grey darken-4">
                  <a href="#" className="brand-logo right">F13X</a>
                  <ul id="nav-mobile" className="right hide-on-med-and-down">
                  </ul>
                </div>
              </nav>
                <div className="container">
                  <div className="row">
                    {contentDisplay}
                    </div>
                    </div>
                    </main>
                </div>
            </div>
            </header>
        );
    }
}
