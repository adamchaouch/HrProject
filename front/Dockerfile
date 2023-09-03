# Utilisez une image Node.js comme base
FROM node:16

ARG WORK_DIR=/frontend
ENV PATH ${WORK_DIR}/node_modules/.bin:$PATH

# Créez un répertoire distinct pour le cache Angular
RUN mkdir -p /frontend/.angular/cache

WORKDIR ${WORK_DIR}

COPY package.json ${WORK_DIR}
COPY package-lock.json ${WORK_DIR}



# Utilisez l'utilisateur root pour l'installation globale

RUN npm install -g @angular/cli


RUN npm install

COPY . ${WORK_DIR}

EXPOSE 4200
RUN chown -R node:node ${WORK_DIR}
USER 1000:1000

CMD npm start
