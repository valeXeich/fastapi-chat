from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from db.base_class import Base


user_room_table = Table(
    'user_room', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.user_id')),
    Column('room_id', Integer, ForeignKey('rooms.room_id'))
)


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)

    rooms = relationship('Room', secondary=user_room_table, back_populates='users')
    messages = relationship('Message', back_populates='user')


class Room(Base):
    __tablename__ = 'rooms'
    room_id = Column(Integer, primary_key=True, autoincrement=True)

    users = relationship('User', secondary=user_room_table, back_populates='rooms')
    messages = relationship('Message', back_populates='room')


class Message(Base):
    __tablename__ = 'messages'
    message_id = Column(Integer, primary_key=True, autoincrement=True)
    file = Column(String(255), nullable=True)
    content = Column(String(255), nullable=False)

    user_id = Column(Integer, ForeignKey('users.user_id'))
    room_id = Column(Integer, ForeignKey('rooms.room_id'))

    user = relationship('User', back_populates='messages')
    room = relationship('Room', back_populates='messages')