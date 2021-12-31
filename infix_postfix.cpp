#include <bits/stdc++.h>
using namespace std;

int precedence(char ch){
    if(ch == '^'){
        return 3;
    }else if(ch == '*' || ch == '/'){
        return 2;
    }else if(ch == '+' || ch == '-'){
        return 1;
    }else{
        return -1;
    }
}


string intfix_to_postfix(string s){
    string result;
    stack<char> stack;
    for (int i = 0; i < s.length(); i++)
    {
        char c = s[i];
        if((c >= 'a' && c <='z') || (c >= 'A' && c<= 'Z') || (c >= '0' && c <= '9')){
            result += c;
        }else if(c == '('){
            stack.push('(');
        }else if(c == ')'){
            while(stack.top() != '('){
                result += stack.top();
                stack.pop();
            }
            stack.pop();
        }else if(stack.empty() || precedence(c) >= precedence(stack.top())){
            stack.push(c);
        }else{
            while (precedence(stack.top()) > precedence(c))
            {
                result += stack.top();
                stack.pop();
            }
            stack.push(c);
        }
    }
    while (!stack.empty())
    {
        result += stack.top();
        stack.pop();
    }
    return result;
}

int main(){
    string infix = "a+b";
    string postfix = intfix_to_postfix(infix);
    cout<<"The ans is "<<postfix<<'\n';
    return 0;
}