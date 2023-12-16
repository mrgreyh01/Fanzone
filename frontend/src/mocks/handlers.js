import { rest } from "msw";

const baseURL = "https://drf-fanzone.herokuapp.com/";

export const handlers = [
    rest.get(`${baseURL}dj-rest-auth/user/`, (req,res,ctx) => {
        return res(ctx.json())
    }),
];
