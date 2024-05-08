schema = """
    create table company
    (
        id         bigint auto_increment
            primary key,
        name       varchar(255) null
    );

    create table deal
    (
        id         bigint auto_increment
            primary key,
        company_id bigint       null,
        constraint FKg8gdn4tnjy2lxovixbxsblrc4
            foreign key (company_id) references company (id)
    );

    create table organization
    (
        organization_id bigint       not null
            primary key,
        name            varchar(255) null
    );

    create table member
    (
        member_id       bigint auto_increment
            primary key,
        authority       enum ('ROLE_ADMIN', 'ROLE_USER')          null,
        email           varchar(255)                              null,
        password        varchar(255)                              null,
        phone_number    varchar(255)                              null,
        status          enum ('ACTIVE', 'INACTIVE', 'WITHDRAWAL') null,
        username        varchar(255)                              null,
        organization_id bigint                                    null,
        constraint FKlfkumie1qe5t7usigehe0yjyk
            foreign key (organization_id) references organization (organization_id)
    );

    create table organization_seq
    (
        next_val bigint null
    );

    create table sheet
    (
        id   bigint auto_increment
            primary key,
        name varchar(255) null
    );

    create table attribute
    (
        id       bigint auto_increment
            primary key,
        name     varchar(255)                                                                             null,
        type     enum ('CHECKBOX', 'CURRENCY', 'DATE', 'MULTISELECT', 'NUMBER', 'SELECT', 'TEXT', 'USER') null,
        sheet_id bigint                                                                                   null,
        constraint FKm12wlqc05ov79o4tpleggxc9n
            foreign key (sheet_id) references sheet (id)
    );

    create table content
    (
        id           bigint auto_increment
            primary key,
        value        varchar(255) null,
        attribute_id bigint       null,
        deal_id      bigint       null,
        constraint UK_q1p3x21bro23oulsob6i39c6o
            unique (attribute_id),
        constraint FKhiopoepfmoin2mg7kn1a3uy2j
            foreign key (deal_id) references deal (id),
        constraint FKjqeq34fxt4iu01ayynvl8368v
            foreign key (attribute_id) references attribute (id)
    );
"""