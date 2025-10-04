const hello = () => {
    const onClick = () => {alert("Hello, React and TypeScript!");}
    const text = "Hello, React and TypeScript!";
    
    return (
        <div onClick={onClick}> 
            {text}
        </div>
    )
}

export default hello;